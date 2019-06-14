//import the the react components
import React from "react";

//import the scss file
import "./App.scss";

import Results from "./Results"
import "./Results.scss";

//extend the website called "App" as a subclass of the react component
class App extends React.Component {

  //set the states
  state = {
    isBlurred: false,
    isLoadingAnimation: false,
    inputField: "",
    results: "",
    textField: ""
  };

  // method that sets the fading out to true
  // arrow function
  setBlur = () => {
    this.setState({ isBlurred: true, isLoadingAnimation:true },
        ()=>{
          fetch("/poem", {
            method: "POST",
            body: this.state.textField
          }).then((response) => response.text()).then((response) => {
            this.setState({isLoadingAnimation: false, results: response})
          })
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
              onChange={this.onTextFieldChange}
              value={this.state.inputField}
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
          <Results dismissClicked = {this.dismissClicked} themes = {this.state.results}/>: null
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
  //Change the text field to what the user enters
  onTextFieldChange = (e) => {
    this.setState({
      inputField: e.target.value
    });
  }
}

//export all of the rendered and returned code
export default App;
