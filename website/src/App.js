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
                    <div className="textBox">
                        <form action="/action_page.php">
                        <input className="box" type="text" name="userPoem" placeholder="Please Enter Your Poem Here..."></input>
                        </form>
                    </div>
                    <button class="button">Enter</button>
                    <img className="leftTriangle" src="./leftTriangle.png"/>
                    <img className="rightTriangle" src="./rightTriangle.png"/>

                </div>
            </div>
        );
    }
}

export default App;
