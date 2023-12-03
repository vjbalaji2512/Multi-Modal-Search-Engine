import React from "react";
import "./App.css";
import Home from "./pages/Home";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Search from "./components/Search";
import SearchPage from "./pages/SearchPage";
import SearchImage from "./pages/SearchImage";

function App() {
  return (
    <div className="app">
      <Router>
        <Switch>
          <Route path="/search">
            <SearchPage />
          </Route>
          <Route path="/image">
            <SearchImage />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

