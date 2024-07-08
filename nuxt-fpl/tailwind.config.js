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
        'fieldh': '55rem',
      },
      width: {
        'fieldw': '35rem',
      },
      inset: {
        "goal": "4em",
        "def": "12em",
        "mid": "20em",
        "att": "28em"
      }
    },
  },
  plugins: [],
}

