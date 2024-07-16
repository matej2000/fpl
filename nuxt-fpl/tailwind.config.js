/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
  ],
  theme: {
    extend: {
      height: {
        'fieldh': '50rem',
      },
      width: {
        'fieldw': '40rem',
      },
      inset: {
        "goal": "4em",
        "def": "12em",
        "mid": "20em",
        "att": "28em"
      },
      colors: {
        'pl-primary': '#00ff85',
        'pl-secondary': '#38003c',
        'pl-third': '#04f5ff'
      },
    },
  },
  plugins: [],
}

