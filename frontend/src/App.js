import './App.css';
import {useState} from 'react';
import styled from "styled-components";
import axios from "axios";
import React from 'react';

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

//선택된 아이템 값은 selectedItem에 들어 있어, 이를 토대로 향후 아이템 값을 적용할 수 있음

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
      LOL_MDC has Analysis League of Legends' Skill Damage Calculator.
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
  const [inputValue, setInputValue] = useState('');
  const [inputItem, setInputItem] = useState('');

  const handleInputChange = (e) => {
    const { value } = e.target;
  };
  const handleReset = () => {
    setInputValue('');
  };
  const handleSum = (inputvalue,data) => {
    alert("계산")
    axios
      .post("http://localhost:8000/test/", {
        name:"아리",
        combo: inputvalue,
        item: "마법사의 지팡이",
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
  };

  return <article>
    <h1>Skill</h1>
    <div>
      <p>Select Your Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/champions/Akali.png'} alt=""/>
      <MainContainer>
        <p><InputBar type = 'text' value = {inputValue} onChange={handleInputChange} /></p>
        <ButtonContainer>
        <Button onClick={handleClick1}>Q</Button>
        <Button onClick={handleClick2}>W</Button>
        <Button onClick={handleClick3}>E</Button>
        <Button onClick={handleClick4}>R</Button>
        <Button onClick={handleClick5}>평타</Button>
        <p><CalButton onClick={handleReset}>Reset</CalButton></p>
        </ButtonContainer>
      </MainContainer>
      <p>{inputValue && <p>Combo: {inputValue}</p>}</p>
      <p><h2>Item Search</h2></p>
      <SearchSelect data={data} />
      <p>Verse.</p>
      <p>Select Your Opposite Champion and its State</p>
      <img src={process.env.PUBLIC_URL + '/img/champions/Aatrox.png'} alt=""/>
      <p><CalButton onClick={()=>{handleSum(inputValue,data)}}>Analysis</CalButton></p>
    </div>
  </article>
}

function App() {
  let content = <Create1></Create1>;
  return (
    <div>
      <Header></Header>
      <Article1></Article1>
      <Article2></Article2>
      <Nav></Nav>
      {content}
    </div>
  );
}

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