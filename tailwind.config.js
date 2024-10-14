/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './polls/templates/**/*.html', // Pointing to the 'polls' app templates
    './mysite/templates/**/*.html', // Global templates (optional)
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
