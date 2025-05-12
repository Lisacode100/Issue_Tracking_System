import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { useEffect } from 'react';


function App() {
    const [count, setCount] = useState(0)
    const [DATA, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/hello/')
    .then((response) => response.json())
    .then((data) => setData(data))
    .catch((err) => console.error('Error fetching data:',err))
    }, []);
   


  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <p>Data fetched: {DATA ? JSON.stringify(DATA) : 'Loading...'}</p>
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
