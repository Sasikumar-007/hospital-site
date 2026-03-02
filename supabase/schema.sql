create table if not exists users (
  id uuid primary key,
  role text not null check (role in ('admin', 'doctor', 'therapist', 'patient')),
  full_name text not null,
  created_at timestamptz default now()
);

create table if not exists patients (
  id uuid primary key references users(id),
  age int,
  gender text,
  history jsonb default '{}'::jsonb
);

create table if not exists doctors (
  id uuid primary key references users(id),
  specialization text,
  experience_years int
);

create table if not exists therapists (
  id uuid primary key references users(id),
  specializations text[] default '{}',
  available boolean default true
);

create table if not exists appointments (
  id bigserial primary key,
  patient_id uuid references patients(id),
  doctor_id uuid references doctors(id),
  appointment_date timestamptz not null,
  status text default 'scheduled',
  symptoms text[] default '{}'
);

create table if not exists therapies (
  id bigserial primary key,
  appointment_id bigint references appointments(id),
  therapist_id uuid references therapists(id),
  therapy_name text not null,
  progress text default 'assigned',
  notes text,
  ai_result jsonb default '{}'::jsonb
);

create table if not exists prescriptions (
  id bigserial primary key,
  appointment_id bigint references appointments(id),
  doctor_id uuid references doctors(id),
  medicines jsonb default '[]'::jsonb,
  diet_advice text,
  instructions text,
  created_at timestamptz default now()
);

alter table users enable row level security;
alter table patients enable row level security;
alter table doctors enable row level security;
alter table therapists enable row level security;
alter table appointments enable row level security;
alter table therapies enable row level security;
alter table prescriptions enable row level security;

create policy "admin full access users" on users for all
using ((auth.jwt() ->> 'role') = 'admin');

create policy "patient own record" on patients for select
using (id = auth.uid() or (auth.jwt() ->> 'role') = 'admin');

create policy "doctor assigned appointments" on appointments for select
using (
  doctor_id = auth.uid() or
  patient_id = auth.uid() or
  (auth.jwt() ->> 'role') = 'admin'
);

create policy "therapist assigned therapies" on therapies for select
using (
  therapist_id = auth.uid() or
  (auth.jwt() ->> 'role') = 'admin'
);
