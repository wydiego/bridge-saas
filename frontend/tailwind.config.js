/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        'bridge-blue': '#2B3A67',
        'bridge-blue-light': '#2F5EAB',
        'bridge-gray': '#2C2F3A',
      },
    },
  },
  plugins: [],
}
