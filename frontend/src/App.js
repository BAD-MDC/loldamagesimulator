
import './App.css';
import {useState} from 'react';

import React from 'react';

//import "bootstrap/dist/css/bootstrap.min.css";

const SearchSelect = ({ data }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredData, setFilteredData] = useState(data);
  const [selectedItem, setSelectedItem] = useState(null);

  const handleSearch = (e) => {
    const searchTerm = e.target.value;
    setSearchTerm(searchTerm);

    // 검색어를 사용하여 데이터를 필터링합니다.
    const filteredData = data.filter(item =>
      item.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredData(filteredData);
  };

  const handleSelectItem = (item) => {
    setSelectedItem(item);
    // 선택된 항목을 다른 곳에서 사용하거나 저장할 수 있습니다.
    console.log('선택된 항목:', item);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="검색어를 입력하세요"
        value={searchTerm}
        onChange={handleSearch}
      />
      <ul>
        {filteredData.map(item => (
          <li key={item} onClick={() => handleSelectItem(item)}>
            {item}
          </li>
        ))}
      </ul>
      {selectedItem && <p>선택된 아이템: {selectedItem}</p>}
    </div>
  );
};

const data = [
    'Hextech Rocketbelt',
    'Shadowflame',
    'Zhonyas Hourglass',
    'Rabaons Deathcap',
    'Void Staff',
    'Socerers Shoes',
  ];

function Header(){
  return <header>
    <h1 ><a href="/">LOL_MDC</a></h1>
  </header>
}

function Article1(){
  return <article>
    <h2>Welcome to LOL_MDC</h2>
      LOL_MDC has 4 Component, Expected Team Winning Rate, Expected Of Line Match, Comparison Within Tier and Analysis Skill Damage.
  </article>
}

function Article2(){
  return <article>
    This Page is made by BAD-MDC, People who leave the Air Force training camp for health problems and find a New Way.
  </article>
}

function Nav(props){
  return <nav>
    <ol>

    </ol>
  </nav>
}

function Create1(){
  return <article>
    <h2>Expected Team Winning Rate</h2>
    <form>
      <p><input type="text" name="title" placeholder="Champion1"></input></p>
      <p><input type="text" name="title" placeholder="Champion2"></input></p>
      <p><input type="text" name="title" placeholder="Champion3"></input></p>
      <p><input type="text" name="title" placeholder="Champion4"></input></p>
      <p><input type="text" name="title" placeholder="Champion5"></input></p>
      <p><input type = "submit" value = "Caculate"></input></p>
    </form>
  </article>
}

function Create2(){
  return <article>
    <h2>Expected Of Line Match</h2>
    <form>
      <p><input type="text" name="title" placeholder="Champion1"></input></p>
      <p><input type="text" name="title" placeholder="Champion2"></input></p>
      <p><input type = "submit" value = "Caculate"></input></p>
    </form>
  </article>
}

function Create3(){
  return <article>
    <h2>Comparsion Within Tier</h2>
    <form>
      <p><input type="text" name="title" placeholder="Champion1"></input></p>
      <p><input type="text" name="title" placeholder="Champion2"></input></p>
      <p><input type = "submit" value = "Caculate"></input></p>
    </form>
  </article>
}

function Create4(){
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };
  const handleReset = () => {
    setInputValue('');
  };
  const handleSum = () => {
    alert('미구현')
    //inputValue가 string으로 입력받아 이를 BE에 넘겨서 계산
  }

  const handleClick1 = () => {
    setInputValue(inputValue + 'Q');
  };
  const handleClick2 = () => {
    setInputValue(inputValue + 'W');
  };
  const handleClick3 = () => {
    setInputValue(inputValue + 'E');
  };
  const handleClick4 = () => {
    setInputValue(inputValue + 'R');
  };
  const handleClick5 = () => {
    setInputValue(inputValue + '평');
  };

  return <article>
    <h1>Skill</h1>
    <div>
      <p>Select Your Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/champions/Akali.png'} alt=""/>
      <p><input type = 'text' value = {inputValue} onChange={handleInputChange} /></p>
      <button onClick={handleClick1}>Q</button>
      <button onClick={handleClick2}>W</button>
      <button onClick={handleClick3}>E</button>
      <button onClick={handleClick4}>R</button>
      <button onClick={handleClick5}>평타</button>
      <p><button onClick={handleReset}>Reset</button></p>
      <h2>Item Search</h2>
      <SearchSelect data={data} />
      <p>Verse.</p>
      <p>Select Your Opposite Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/champions/Aatrox.png'} alt=""/>
      <p><button onClick={handleSum}>Analysis</button></p>
    </div>
  </article>
}

function App() {
  const [mode, setMode] = useState('e');

  let content = null;

  if(mode === 'CREATE1'){
    content = <Create1></Create1>
  }
  else if(mode === 'CREATE2'){
    content = <Create2></Create2>
  }
  else if(mode === 'CREATE3'){
    content = <Create3></Create3>
  }
  else if (mode === 'CREATE4'){
    content = <Create4></Create4>
  }

  return (
    <div>
      <Header></Header>
      <Article1></Article1>
      <Article2></Article2>
      <Nav></Nav>

      {content}
      <p><a href="/1. Expected Team Winning Rate" onClick={event=>{
        event.preventDefault();
        setMode('CREATE1');
      }}>Expected Team Winning Rate</a></p>
      <p><a href="/2. Expected Of Line Match" onClick={event=>{
        event.preventDefault();
        setMode('CREATE2');
      }}>Expected Of Line Match</a></p>
      <p><a href="/3. Comparison Within Tier" onClick={event=>{
        event.preventDefault();
        setMode('CREATE3');
      }}>Comparison Within Tier</a></p>
      <p><a href="/4. Skill" onClick={event=>{
        event.preventDefault();
        setMode('CREATE4');
      }}>Skill</a></p>

    </div>
  );
}

export default App;

