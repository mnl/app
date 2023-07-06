import { render, screen } from '@testing-library/react';
import App from './App';

test('renders api link', () => {
  render(<App />);
  const linkElement = screen.getByText(/api/i);
  expect(linkElement).toBeInTheDocument();
});
