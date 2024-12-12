import React from 'react';

function AdList({ ads, deleteAd }) {
  return (
    <div>
      <h2>Список объявлений</h2>
      {ads.length === 0 ? (
        <p>Нет объявлений.</p>
      ) : (
        <ul>
          {ads.map(ad => (
            <li key={ad.id} style={{ marginBottom: '10px' }}>
              <strong>{ad.title}</strong>: {ad.description}
              <button
                onClick={() => deleteAd(ad.id)}
                style={{ marginLeft: '10px' }}
              >
                Удалить
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default AdList;
