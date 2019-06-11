//import the the react components
import React from "react";

//import the scss file
import "./Results.scss";

//extend the websitite called "App" as a subclass of the react component

class Results extends React.Component {
    // method that sets the fading out to true
    // arrow function
    dismissClicked = () => {
        this.props.dismissClicked();
    }

    render() {

        //create a style of bluring the page if fadingOut is tru

        return (
            <div className="background-box">
                <div className="results-header">Themes:</div>
                <div className="results-field">Theme 1, Theme 2, Theme 3, Theme 4, Theme 5</div>
                <button className="dismiss-button" onClick={this.dismissClicked}>Dismiss</button>
            </div>
        );
    }
}

//export all of the rendered and returned code
export default Results;