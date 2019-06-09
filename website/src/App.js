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
        <div style={loaderStyle}><div className="loader"/></div>
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
  
  const loaderStyle = {
    position: "absolute", // or position: "fixed"
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    display: "flex",
    justifyContent: "center",
    alignItems: "center"
  };

export default App;
