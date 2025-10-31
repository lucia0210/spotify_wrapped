import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/api/getData")
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div className="min-h-screen bg-spotifyBlack text-white p-8 font-sans">
      <h1 className="text-4xl font-bold text-spotifyGreen mb-6">Predice tu Wrapped 🎧</h1>
      <table className="w-full border-collapse">
        <thead>
          <tr className="border-b border-gray-600">
            <th className="p-2 text-left">Usuario</th>
            <th className="p-2 text-left">Artista</th>
            <th className="p-2 text-left">Género</th>
            <th className="p-2 text-left">Minutos</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i} className="border-b border-gray-700 hover:bg-gray-800">
              <td className="p-2">{row.user}</td>
              <td className="p-2">{row.top_artist}</td>
              <td className="p-2">{row.top_genre}</td>
              <td className="p-2">{row.minutes_listened}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

