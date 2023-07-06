import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          My frontend app
        </p>
        <a
          className="App-link"
          href="/api"
          target="_blank"
          rel="noopener noreferrer"
        >
          API
        </a>
      </header>
    </div>
  );
}

export default App;
