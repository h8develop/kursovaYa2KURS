import React, { useState, useEffect } from 'react';
import AdList from './components/AdList';
import axios from 'axios';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';

axios.defaults.baseURL = 'http://backend.local';

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
    <Router basename="/">
      <div style={{ padding: '20px' }}>
        <h1>Система управления рекламными кампаниями</h1>
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/" style={{ marginRight: '20px' }}>Главная</Link>
          <Link to="/dashboard">Аналитика</Link>
        </nav>
        <Routes>
          <Route 
            path="/" 
            element={
              <>
                <h2>Создать объявление</h2>
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
                <AdList ads={ads} deleteAd={deleteAd} />
              </>
            }
          />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
