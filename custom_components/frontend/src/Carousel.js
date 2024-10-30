import React from 'react';
import Slider from 'react-slick';
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
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

  handleKeyDown = (event) => {
    if (event.key === 'ArrowLeft') {
      this.sliderRef.current.slickPrev();
    } else if (event.key === 'ArrowRight') {
      this.sliderRef.current.slickNext();
    }
  };

  render() {
    const { height, width, slides } = this.props.args; // Receive slides data
    const settings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      accessibility: true,
      pauseOnHover: true,
      swipe: true,
    };

    return (
      <div className="carousel-container" style={{ width: width || '80%' }}>
        <h2>Customizable Carousel</h2>
        <Slider ref={this.sliderRef} {...settings}>
          {slides.map((slide, index) => (
            <div
              key={index}
              className={`carousel-slide ${slide.type === 'text' ? 'text-slide' : ''}`}
              style={{ height: height || '100px' }}
            >
              {slide.type === 'image' ? (
                <img src={slide.content} alt={`Slide ${index + 1}`} />
              ) : (
                <h3 style={{ height: height || '100px' }}>{slide.content}</h3>
              )}
            </div>
          ))}
        </Slider>
      </div>
    );
  }
}

export default withStreamlitConnection(Carousel); 