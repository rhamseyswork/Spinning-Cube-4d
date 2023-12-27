import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

// Use the static files from the current directory
app.use(express.static(path.join(__dirname, '.')));

// Other express setup...

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
