import Sidebar from '../components/Sidebar';
import StatCard from '../components/StatCard';
import TableCard from '../components/TableCard';

const stats = [
  { label: 'Total Patients', value: '1,204' },
  { label: 'Total Doctors', value: '34' },
  { label: 'Total Therapists', value: '57' },
  { label: 'Total Appointments', value: '2,489' }
];

const appointments = [
  ['APT-1120', 'Kavya N', 'Dr. Sharma', 'Vata', 'Scheduled'],
  ['APT-1121', 'Ramesh P', 'Dr. Menon', 'Pitta', 'In Progress'],
  ['APT-1122', 'Priya R', 'Dr. Nair', 'Kapha', 'Completed']
];

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-slate-50 p-4 lg:p-6">
      <div className="max-w-7xl mx-auto grid lg:grid-cols-[256px_1fr] gap-4">
        <Sidebar />
        <main className="space-y-4">
          <div className="bg-white rounded-card shadow-sm p-4">
            <h2 className="text-xl font-bold text-slate-900">Healthcare Analytics</h2>
            <p className="text-slate-500 text-sm">AI-powered Panchakarma operations overview</p>
          </div>

          <section className="grid sm:grid-cols-2 xl:grid-cols-4 gap-4">
            {stats.map((item) => (
              <StatCard key={item.label} label={item.label} value={item.value} />
            ))}
          </section>

          <TableCard
            title="Today's Appointments"
            headers={['Appointment', 'Patient', 'Doctor', 'Dominant Dosha', 'Status']}
            rows={appointments}
          />
        </main>
      </div>
    </div>
  );
}
