const navItems = [
  'Admin Dashboard',
  'Appointments',
  'Dosha Analysis',
  'Therapists',
  'Therapies',
  'Reports'
];

export default function Sidebar() {
  return (
    <aside className="w-full lg:w-64 bg-white shadow-sm rounded-card p-4">
      <h1 className="text-xl font-bold text-medicalBlue">Panchakarma PMS</h1>
      <p className="text-sm text-slate-500 mb-6">SIH25023</p>
      <nav className="space-y-2">
        {navItems.map((item) => (
          <button
            key={item}
            className="w-full text-left px-3 py-2 rounded-lg text-sm text-slate-700 hover:bg-blue-50 hover:text-medicalBlue transition"
          >
            {item}
          </button>
        ))}
      </nav>
    </aside>
  );
}
