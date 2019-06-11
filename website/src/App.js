//import the the react components
import React from "react";

//import the scss file
import "./App.scss";

import Results from "./Results"
import "./Results.scss";

//extend the websitite called "App" as a subclass of the react component
class App extends React.Component {

  //set the fadingOut state as false
  state = { 
    isBlurred: false,
    isLoadingAnimation: false,
  };

  // method that sets the fading out to true
  // arrow function
  setBlur = () => {
    this.setState({ isBlurred: true, isLoadingAnimation:true },
        ()=>{
          setTimeout(() => {
            this.setState({isLoadingAnimation: false})
          },2500);
        }
      );
    

  }

  dismissClicked = () => {
    this.setState({ isBlurred: false });
  }

  //render all of the following code for the webpage
  render() {

    //create a style of bluring the page if fadingOut is true
    const contentStyle = this.state.isBlurred
      ? { filter: "blur(0.35vw)" }
      : undefined;

    //return the code and display it to the webpage
    return (
      //create the entire webpage and call it "App"
      <div className="App" style={{ position: "relative" }}>
        <div style={contentStyle}>
          <div className="top-bar">
            <div className="title">.datapoems</div>
            <img className="logo" src="./logo.png" />
          </div>
          <div className="container">
            <div className="slogan-line-one">Poem Theme</div>
            <div className="slogan-line-two">Detector</div>
            <textarea
              className="input-field"
              placeholder="Please Enter Your Poem Here..."
            />
            <button className="button" onClick={this.setBlur}>
              Enter
            </button>
            <img className="left-triangle" src="./leftSideTriangle.png" />
            <img className="right-triangle" src="./rightSideTriangle.png" />
          </div>
        </div>
        {
          (this.state.isBlurred && !this.state.isLoadingAnimation) ?
          <Results dismissClicked = {this.dismissClicked}/>: null
        }
        {
          this.state.isLoadingAnimation ? 
            <div className="loader-style"></div>
            :
            ""
        }
        </div>
    );
  }
}

//export all of the rendered and returned code
export default App;
