import './App.css';
import {useState} from 'react';
import styled from "styled-components";
import axios from "axios";
import React from 'react';

const data = [
    'Hextech Rocketbelt',
    'Shadowflame',
    'Zhonyas Hourglass',
    'Rabaons Deathcap',
    'Void Staff',
    'Socerers Shoes',
  ];

function Create1(){
  function Header(){
    return <header>
      <h1 ><a href="/">LOL_MDC</a></h1>
    </header>
  }
  function Article(){
    return <article>
      <h2>Welcome to LOL_MDC</h2>
      LOL_MDC has Analysis League of Legends' Skill Damage Calculator.
      <p>This Page is made by BAD-MDC, People who leave the Air Force training camp for health problems and find a New Way.</p>
    </article>
  }

  const [inputValue, setInputValue] = useState('');
  const [inputItem, setInputItem] = useState('');

  const handleInputChange = (e) => {
    const { value } = e.target;
  };
  const handleReset = () => {
    setInputValue('');
  };

  function LevelSelector(){
    const [selectedLevel, setSelectedLevel] = useState('');
    const handleLevelChange = (event) => {
    setSelectedLevel(event.target.value);
  };
    return (
    <div>
      <select value={selectedLevel} onChange={handleLevelChange}>
        <option value="">레벨을 선택하세요</option>
        <option value="1">Level 1</option>
        <option value="3">Level 3</option>
        <option value="6">Level 6</option>
        <option value="16">Level 16</option>
        <option value="18">Level 18</option>
      </select>
      {selectedLevel && <p>You selected Level {selectedLevel}</p>}
    </div>
  );
};

  function QLevelSelector(){
    const [selectedQLevel, setSelectedQLevel] = useState('');
    const handleQLevelChange = (event) => {
    setSelectedQLevel(event.target.value);
  };
    return (
    <div>
      <select value={selectedQLevel} onChange={handleQLevelChange}>
        <option value="">Q Level</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
      {selectedQLevel && <p> Q Level : {selectedQLevel}</p>}
    </div>
  );
};
  function WLevelSelector(){
    const [selectedWLevel, setSelectedWLevel] = useState('');
    const handleWLevelChange = (event) => {
    setSelectedWLevel(event.target.value);
  };
    return (
    <div>
      <select value={selectedWLevel} onChange={handleWLevelChange}>
        <option value="">W Level</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
      {selectedWLevel && <p> W Level : {selectedWLevel}</p>}
    </div>
  );
};
function ELevelSelector(){
    const [selectedELevel, setSelectedELevel] = useState('');
    const handleELevelChange = (event) => {
    setSelectedELevel(event.target.value);
  };
    return (
    <div>
      <select value={selectedELevel} onChange={handleELevelChange}>
        <option value="">E Level</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
      {selectedELevel && <p> E Level : {selectedELevel}</p>}
    </div>
  );
};
function RLevelSelector(){
    const [selectedRLevel, setSelectedRLevel] = useState('');
    const handleRLevelChange = (event) => {
    setSelectedRLevel(event.target.value);
  };
    return (
    <div>
      <select value={selectedRLevel} onChange={handleRLevelChange}>
        <option value="">R Level</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
      </select>
      {selectedRLevel && <p> R Level : {selectedRLevel}</p>}
    </div>
  );
};
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
      <InputBar
        type="text"
        placeholder="검색할 아이템 이름을 입력하세요"
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
      {}
    </div>
  );
};
  const handleSum = (inputValue,data,selectedLevel,selectedItem) => {
    alert("계산")
    axios
      .post("http://localhost:8000/test/", {
        name:"아리",
        combo: inputValue,
        level: selectedLevel,
        /* qlevel: selectedQLevel,
        wlevel: selectedWLevel,
        elevel: selectedELevel,
        rlevel: selectedRLevel,
        */
        item: selectedItem,
      })
    .then((response) => {
        if (response.status < 300) {
          console.log(response.data);
          alert(response.data['data']);
        }
      });
    //inputValue가 string으로 입력받아 이를 BE에 넘겨서 계산
  };

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
  const handleClick6 = () =>{
    setInputItem(inputItem);
  }; //향후 아이템 개수 늘어날 때 사용

  return <article>
    <MaeContainer>
    <Header />
    <Article />
    <h1>Skill</h1>
      </MaeContainer>
    <div>
      <p>Select Your Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/champions/Akali.png'} alt=""/>
      <MainContainer>
        <p><InputBar type = 'text' value = {inputValue} onChange={handleInputChange} /></p>
        <LevelSelector />
        <QLevelSelector />
        <WLevelSelector />
        <ELevelSelector />
        <RLevelSelector />
        <ButtonContainer>
        <Button onClick={handleClick1}>Q</Button>
        <Button onClick={handleClick2}>W</Button>
        <Button onClick={handleClick3}>E</Button>
        <Button onClick={handleClick4}>R</Button>
        <Button onClick={handleClick5}>평타</Button>
        <p><CalButton onClick={handleReset}>Reset</CalButton></p>
        </ButtonContainer>
      <p>{inputValue && <p>Combo: {inputValue}</p>}</p>
      <p><h2>Item Search</h2></p>
      <SearchSelect data={data} />
      <p>Verse.</p>
      <p>Select Your Opposite Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/champions/Aatrox.png'} alt=""/>
      <p><CalButton onClick={()=>{handleSum(inputValue,data)}}>Analysis</CalButton></p>
        </MainContainer>
    </div>
  </article>
}

function App() {
  let content = <Create1></Create1>;
  return (
    <div>
      {content}
    </div>
  );
}

const MaeContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 30vh;
`;

const MainContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 30vh;
`;

const ButtonContainer = styled.div`
  display: grid;
  width: 40%;
  max-width: 450px;
  height: 20%;
  grid-template-columns: repeat(5, 1fr);
  grid-column-gap: 5px;
  grid-row-gap: 5px;
`;

const Button = styled.button`
  background-color: #f2f3f5;
  border: none;
  color: black;
  font-size: 1.5rem;
  border-radius: 35px;
  cursor: pointer;
  box-shadow: 2px 2px 2px lightgray;

  &:active {
    margin-left: 1px;
    margin-top: 1px;
    box-shadow: none;
  }
`;

const CalButton = styled(Button)`
  font-size: 2rem;
  color: white;
  background-color: #4b89dc;
`;

const InputBar = styled.input`
  width: 50%;
  max-width: 450px;
  height: 25px;
  margin-bottom: 5px;
  border-radius: 10px;
  font-size: 20px;
  border: 2px solid #4b89dc;
  text-align: center;
  padding-right: 10px;
  &:focus {
    outline: none;
  }
`;

export default App;