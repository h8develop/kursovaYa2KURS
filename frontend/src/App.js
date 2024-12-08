import React, { useState, useEffect } from 'react';
import AdList from './components/AdList';
import axios from 'axios';

function App() {
  const [ads, setAds] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  useEffect(() => {
    fetchAds();
  }, []);

  const fetchAds = async () => {
    try {
      const response = await axios.get('/ads/');
      setAds(response.data);
    } catch (error) {
      console.error('Ошибка при получении объявлений:', error);
    }
  };

  const createAd = async () => {
    try {
      const response = await axios.post('/ads/', { title, description });
      setAds([...ads, response.data]);
      setTitle('');
      setDescription('');
    } catch (error) {
      console.error('Ошибка при создании объявления:', error);
    }
  };

  const deleteAd = async (id) => {
    try {
      await axios.delete(`/ads/${id}`);
      setAds(ads.filter(ad => ad.id !== id));
    } catch (error) {
      console.error('Ошибка при удалении объявления:', error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Система Управления Рекламными Кампаниями</h1>
      <div style={{ marginBottom: '20px' }}>
        <h2>Создать Объявление</h2>
        <input
          type="text"
          placeholder="Название"
          value={title}
          onChange={e => setTitle(e.target.value)}
          style={{ marginRight: '10px' }}
        />
        <input
          type="text"
          placeholder="Описание"
          value={description}
          onChange={e => setDescription(e.target.value)}
          style={{ marginRight: '10px' }}
        />
        <button onClick={createAd}>Создать</button>
      </div>
      <AdList ads={ads} deleteAd={deleteAd} />
    </div>
  );
}

export default App;
