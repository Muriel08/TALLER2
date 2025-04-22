// src/components/ClienteList.js
import React, { useEffect, useState } from 'react';
import API from '../api';

const ClienteList = ({ onSelect }) => {
  const [clientes, setClientes] = useState([]);

  const obtenerClientes = async () => {
    const res = await API.get('/clientes');
    setClientes(res.data);
  };

  const eliminarCliente = async (id) => {
    await API.delete(`/clientes/${id}`);
    obtenerClientes();
  };

  useEffect(() => {
    obtenerClientes();
  }, []);

  return (
    <div>
      <h2>Lista de Clientes</h2>
      <ul>
        {clientes.map((c) => (
          <li key={c.id}>
          {c.nombre} ({c.email}){' '}
          <button onClick={() => onSelect(c)}>Editar</button>
          <button onClick={() => eliminarCliente(c.id)}>Eliminar</button>
        </li>
        
        ))}
      </ul>
    </div>
  );
};

export default ClienteList;
