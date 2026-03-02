export default function StatCard({ label, value }) {
  return (
    <div className="bg-white rounded-card shadow-sm p-4">
      <p className="text-sm text-slate-500">{label}</p>
      <p className="text-2xl font-semibold text-slate-900">{value}</p>
    </div>
  );
}
