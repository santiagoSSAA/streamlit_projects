import React from 'react';
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import { CheckIcon } from '@heroicons/react/20/solid';
class Pricing extends React.Component {
  componentDidMount() {
    Streamlit.setComponentReady();
    Streamlit.setFrameHeight();
  }

  render() {
    const {
      tiers,
      title,
      subtitle,
      description,
      maxWidth,
      theme,
      ctaText,
    } = this.props.args; // Recibe todos los parámetros desde Streamlit

    // Estilos dinámicos basados en el tema
    const themeClasses = theme === 'dark' ? 'bg-gray-900 text-white' : 'bg-white text-gray-900';

    return (
      <div className={`relative isolate ${themeClasses} px-6 py-24 sm:py-32 lg:px-8`} style={{ maxWidth: maxWidth || '100%' }}>
        <div aria-hidden="true" className="absolute inset-x-0 -top-3 -z-10 transform-gpu overflow-hidden px-36 blur-3xl">
          <div
            style={{
              clipPath:
                'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)',
            }}
            className="mx-auto aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30"
          />
        </div>
        <div className="mx-auto max-w-4xl text-center">
          <h2 className="text-base/7 font-semibold text-indigo-600">{title}</h2>
          <p className="mt-2 text-balance text-5xl font-semibold tracking-tight sm:text-6xl">
            {subtitle}
          </p>
        </div>
        <p className="mx-auto mt-6 max-w-2xl text-pretty text-center text-lg font-medium sm:text-xl/8">
          {description}
        </p>
        <div className="mx-auto mt-16 grid max-w-lg grid-cols-1 items-center gap-y-6 sm:mt-20 sm:gap-y-0 lg:max-w-4xl lg:grid-cols-2">
          {tiers.map((tier, tierIdx) => (
            <div
              key={tier.id}
              className={`${
                tier.featured ? 'relative bg-gray-900 shadow-2xl' : 'bg-white/60 sm:mx-8 lg:mx-0'
              } rounded-3xl p-8 ring-1 ring-gray-900/10 sm:p-10`}
            >
              <h3
                id={tier.id}
                className={`${
                  tier.featured ? 'text-indigo-400' : 'text-indigo-600'
                } text-base/7 font-semibold`}
              >
                {tier.name}
              </h3>
              <p className="mt-4 flex items-baseline gap-x-2">
                <span
                  className={`${
                    tier.featured ? 'text-white' : 'text-gray-900'
                  } text-5xl font-semibold tracking-tight`}
                >
                  {tier.priceMonthly}
                </span>
                <span className={`${tier.featured ? 'text-gray-400' : 'text-gray-500'} text-base`}>/month</span>
              </p>
              <p className={`${tier.featured ? 'text-gray-300' : 'text-gray-600'} mt-6 text-base/7`}>
                {tier.description}
              </p>
              <ul
                role="list"
                className={`${
                  tier.featured ? 'text-gray-300' : 'text-gray-600'
                } mt-8 space-y-3 text-sm/6 sm:mt-10`}
              >
                {tier.features.map((feature) => (
                  <li key={feature} className="flex gap-x-3">
                    <CheckIcon
                      aria-hidden="true"
                      className={`${
                        tier.featured ? 'text-indigo-400' : 'text-indigo-600'
                      } h-6 w-5 flex-none`}
                    />
                    {feature}
                  </li>
                ))}
              </ul>
              <a
                href={tier.href}
                aria-describedby={tier.id}
                className={`${
                  tier.featured
                    ? 'bg-indigo-500 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline-indigo-500'
                    : 'text-indigo-600 ring-1 ring-inset ring-indigo-200 hover:ring-indigo-300 focus-visible:outline-indigo-600'
                } mt-8 block rounded-md px-3.5 py-2.5 text-center text-sm font-semibold focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 sm:mt-10`}
              >
                {ctaText || 'Get started today'}
              </a>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default withStreamlitConnection(Pricing); 