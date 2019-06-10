//import the the react components
import React from "react";

//import the scss file
import "./Results.scss";

//extend the websitite called "App" as a subclass of the react component
class Results extends React.Component {

    //set the fadingOut state as false
  state = { fadingOut: false };
  
  // method that sets the fading out to true
  // arrow function
  fadeOut = () => {
    this.setState({ fadingOut: true });
  }

    render() {

        //create a style of bluring the page if fadingOut is true
    const contentStyle = this.state.fadingOut
    ? { filter: "blur(0.35vw)" }
    : undefined;

        return (
            <div className="Results" style={{ position: "relative" }}>
                <div className="pop-up" style={contentStyle}>
                    <div className="background-box" style={{flex: 1, flexDirection: 'column'}}>
                        <button className="dismiss-button" onClick={this.fadeOut}>Dismiss</button>
                    </div>
                </div>
            </div>
        );
    }
}

//export all of the rendered and returned code
export default Results;