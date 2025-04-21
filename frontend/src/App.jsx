import React, { useState } from 'react';
import ClienteList from './components/ClienteList';
import ClienteForm from './components/ClienteForm';
import HalfRating from './components/HalfRating';

function App() {
  const [clienteSeleccionado, setClienteSeleccionado] = useState(null);
  const [recargar, setRecargar] = useState(false);

  const handleRecargar = () => {
    setRecargar(!recargar);
    setClienteSeleccionado(null);
  };

  return (
    <div className="App">
      <h1>Taller Mecánico - Clientes</h1>
      <ClienteForm clienteSeleccionado={clienteSeleccionado} onSuccess={handleRecargar} />
      <ClienteList onSelect={setClienteSeleccionado} key={recargar} />

      <h2>Calificá este servicio:</h2>
      <HalfRating />
    </div>
  );
}

export default App;


