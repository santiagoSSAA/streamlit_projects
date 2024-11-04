import React from 'react';
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import './Carousel.css';

class Carousel extends React.Component {
  constructor(props) {
    super(props);
    this.sliderRef = React.createRef();
  }

  componentDidMount() {
    Streamlit.setComponentReady();
    Streamlit.setFrameHeight();
  }

  render() {
    const { height, width, slides } = this.props.args; // Receive slides data
    return (
      <h1 className="text-3xl font-bold underline">
        Hello world!
      </h1>
    );
  }
}

export default withStreamlitConnection(Carousel); 