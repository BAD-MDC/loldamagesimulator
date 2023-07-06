import React, { useState } from 'react';

const ItemSearch = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [items, setItems] = useState([
    'Hextech Rocketbelt',
    'Shadowflame',
    'Zhonyas Hourglass',
    'Rabaons Deathcap',
    'Void Staff',
    'Socerers Shoes',
  ]);

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const filteredItems = items.filter((item) =>
    item.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      <input
        type="text"
        value={searchQuery}
        onChange={handleSearchChange}
        placeholder="Search for an item"
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default ItemSearch;