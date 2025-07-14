import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import PasteForm from "./components/PasteForm";
import PasteView from "./components/PasteView";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PasteForm />} />
        <Route path="/:id" element={<PasteView />} />
      </Routes>
    </Router>
  );
}

export default App;
