export default function TableCard({ title, headers, rows }) {
  return (
    <section className="bg-white rounded-card shadow-sm p-4 overflow-auto">
      <h2 className="font-semibold text-slate-900 mb-4">{title}</h2>
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-slate-500 border-b">
            {headers.map((head) => (
              <th key={head} className="py-2 pr-3">{head}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, idx) => (
            <tr key={idx} className="border-b last:border-0">
              {row.map((cell, cellIdx) => (
                <td key={cellIdx} className="py-2 pr-3">{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
