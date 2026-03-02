/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        medicalBlue: '#2563EB',
        ayurvedicGreen: '#16A34A'
      },
      borderRadius: {
        card: '12px'
      }
    }
  },
  plugins: []
};
