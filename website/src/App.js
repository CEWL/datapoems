import React from "react";
import "./App.scss";

class App extends React.Component {
    state = { fadingOut: false };
    fadeOut = () => this.setState({ fadingOut: true });
  
    render() {
      const contentStyle = this.state.fadingOut
        ? { filter: "blur(0.35vw)" }
        : undefined;
      const loadingIndicator = this.state.fadingOut ? (
        <div className="loader-style"></div>
      ) : null;
  
      return (
        <div className="App" style={{ position: "relative" }}>
          <div style={contentStyle}>
            <div className="top-bar">
              <div className="title">.datapoems</div>
              <img className="logo" src="./logo.png" />
            </div>
            <div className="container">
              <div className="sloganLineOne">Poem Theme</div>
              <div className="sloganLineTwo">Detector</div>
              <textarea
                className="inputField"
                placeholder="Please Enter Your Poem Here..."
              />
              <button className="button" onClick={this.fadeOut}>
                Enter
              </button>
              <img className="leftTriangle" src="./leftSideTriangle.png" />
              <img className="rightTriangle" src="./rightSideTriangle.png" />
            </div>
          </div>
          {loadingIndicator}
        </div>
      );
    }
  }


export default App;
