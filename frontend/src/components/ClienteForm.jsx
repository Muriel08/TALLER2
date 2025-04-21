// src/components/ClienteForm.js
import React, { useState, useEffect } from 'react';
import API from '../api';

const ClienteForm = ({ clienteSeleccionado, onSuccess }) => {
  const [form, setForm] = useState({
    Nombre: '',
    Apellido: '',
    Telefono: '',
    Direccion: '',
    Email: '',
  });

  useEffect(() => {
    if (clienteSeleccionado) {
      setForm(clienteSeleccionado);
    }
  }, [clienteSeleccionado]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (clienteSeleccionado) {
      await API.put(`/clientes/${clienteSeleccionado.ID_Cliente}`, form);
    } else {
      await API.post('/clientes', form);
    }
    onSuccess();
    setForm({
      Nombre: '',
      Apellido: '',
      Telefono: '',
      Direccion: '',
      Email: '',
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{clienteSeleccionado ? 'Editar Cliente' : 'Crear Cliente'}</h2>
      <input name="Nombre" value={form.Nombre} onChange={handleChange} placeholder="Nombre" required />
      <input name="Apellido" value={form.Apellido} onChange={handleChange} placeholder="Apellido" required />
      <input name="Telefono" value={form.Telefono} onChange={handleChange} placeholder="Teléfono" />
      <input name="Direccion" value={form.Direccion} onChange={handleChange} placeholder="Dirección" />
      <input name="Email" value={form.Email} onChange={handleChange} placeholder="Email" />
      <button type="submit">{clienteSeleccionado ? 'Actualizar' : 'Guardar'}</button>
    </form>
  );
};

export default ClienteForm;
