# Quick Start Guide

Get your Prompt Generator up and running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Node.js 16+ installed
- Terminal/Command Prompt access

## Installation

### 1. Backend Setup (2 minutes)

```bash
# Navigate to project root
cd prompt-generator

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file (optional)
copy backend\.env.example backend\.env  # Windows
cp backend/.env.example backend/.env    # macOS/Linux

# Start backend server
cd backend
python app.py
```

✅ Backend should now be running on `http://localhost:5000`

### 2. Frontend Setup (2 minutes)

Open a **new terminal window**:

```bash
# Navigate to frontend directory
cd prompt-generator/frontend

# Install dependencies
npm install

# Create environment file (optional)
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux

# Start development server
npm start
```

✅ Frontend should automatically open at `http://localhost:3000`

## First Prompt Generation

1. **Choose Modality**: Click on "Image", "Video", or "Voice"
2. **Fill Required Fields**:
   - For Image: Enter subject and style
   - For Video: Enter scene, action, and duration
   - For Voice: Enter text, accent, emotion, and pace
3. **Select Model**: Choose from the dropdown (e.g., DALL-E 3)
4. **Generate**: Click "Generate Prompt"
5. **Copy/Export**: Use buttons to copy or export your prompt

## Quick Tips

### Using Templates

1. Select a modality (e.g., Image)
2. Click the "Quick Start Template" dropdown
3. Choose a template (e.g., "Portrait Photography")
4. Fields auto-fill with preset values
5. Customize as needed and generate

### Saving to History

1. Generate a prompt
2. Click the three-dot menu (⋮) in the result box
3. Select "Save to History"
4. Access history anytime via the "History" button in the header

### Exporting Prompts

**As Text File:**
- Click ⋮ menu → "Export as TXT"

**As JSON File:**
- Click ⋮ menu → "Export as JSON"
- Includes all metadata (model, inputs, timestamp)

## Troubleshooting

### Backend won't start

**Error: Port 5000 already in use**
```bash
# Change port in backend/.env
FLASK_PORT=5001
```

**Error: Module not found**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend won't start

**Error: Port 3000 already in use**
```bash
# Set custom port
set PORT=3001 && npm start  # Windows
PORT=3001 npm start          # macOS/Linux
```

**Error: Cannot connect to backend**
```bash
# Check backend is running on port 5000
# Update frontend/.env if needed
REACT_APP_API_URL=http://localhost:5000
```

### Browser shows blank page

1. Check browser console (F12) for errors
2. Clear cache (Ctrl+Shift+Delete)
3. Try incognito mode
4. Restart development server

## Next Steps

### Customize Your Experience

**Add Custom Templates:**
Edit `frontend/src/config.js`:
```javascript
export const TEMPLATES = {
  image: {
    myCustomTemplate: {
      name: "My Custom Template",
      values: {
        subject: "...",
        style: "...",
      },
    },
  },
};
```

**Adjust Validation Rules:**
Edit `frontend/src/config.js`:
```javascript
export const REQUIRED_FIELDS = {
  image: {
    common: ["subject", "style"],  // Add/remove fields
  },
};
```

**Change Color Scheme:**
Edit CSS files in `frontend/src/styles/`

### Production Deployment

See `README.md` for detailed deployment instructions.

### Run Tests

**Backend:**
```bash
cd backend
pytest
```

**Frontend:**
```bash
cd frontend
npm test
```

## Common Workflows

### Workflow 1: Quick Image Prompt

1. Select "Image"
2. Template: "Portrait Photography"
3. Modify subject: "a software engineer"
4. Generate → Copy

**Time: 30 seconds**

### Workflow 2: Batch Generate with History

1. Generate multiple prompts
2. Save each to history
3. Review in History panel
4. Mark favorites (⭐)
5. Export favorites as JSON

**Time: 2 minutes**

### Workflow 3: Fine-Tune for Specific Model

1. Select modality
2. Choose target model
3. Fill all optional fields
4. Generate and compare results
5. Adjust and regenerate

**Time: 3-5 minutes**

## Keyboard Shortcuts

- **Ctrl/Cmd + K**: Focus model selector
- **Ctrl/Cmd + Enter**: Generate prompt (when in form)
- **Ctrl/Cmd + C**: Copy result (when focused)
- **Escape**: Close history modal

## Resources

- **Full Documentation**: See `README.md`
- **Migration Guide**: See `MIGRATION_GUIDE.md`
- **API Reference**: Check `/health` and `/models` endpoints
- **Support**: Open an issue on GitHub

## Getting Help

**Issue Template:**
```markdown
**Environment:**
- OS: [Windows/macOS/Linux]
- Python Version: [run `python --version`]
- Node Version: [run `node --version`]

**What I tried:**
[Describe what you did]

**Expected:**
[What you expected to happen]

**Actual:**
[What actually happened]

**Error Messages:**
[Paste any error messages]
```

---

**Happy prompt engineering! 🚀**

*Need more features? Check out the full README.md or contribute to the project!*
