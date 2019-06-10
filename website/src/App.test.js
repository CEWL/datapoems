//import all of the websites components
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

//render the webpage for the user
it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});
