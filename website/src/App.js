import React from "react";
import "./App.scss";

class App extends React.Component {
    render() {
        return (
            <div className="App">

                <div className="top-bar">

                <div className="title">
                    .datapoems
                </div>

                <img className="logo" src="./logo.png"/>
                       
                </div>

                <div className="container">
                    <div className="sloganLineOne">Poem Theme</div>
                    <div className="sloganLineTwo">Detector</div>
                    <textarea className="inputField" placeholder="Please Enter Your Poem Here..."></textarea>
                    <button className="button">Enter</button>
                    <img className="leftTriangle" src="./leftSideTriangle.png"/>
                    <img className="rightTriangle" src="./rightSideTriangle.png"/>
                </div>
            </div>
        );
    }
}

export default App;
