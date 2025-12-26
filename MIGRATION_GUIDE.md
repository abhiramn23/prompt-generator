# Migration Guide

This guide helps you migrate from the old version to the improved version of the Prompt Generator.

## Overview of Changes

The improved version includes:
- New component structure with better organization
- Toast notifications instead of alert dialogs
- History and favorites management
- Export functionality
- Template system
- Improved validation and error handling
- Better accessibility

## Step-by-Step Migration

### Option 1: Use New Components Alongside Old (Recommended)

The new components are in separate files, so you can test them without breaking existing functionality:

1. **Keep existing App.js** for backward compatibility
2. **Use ImprovedApp.jsx** for new features
3. **Update index.js** to switch between versions:

```javascript
// frontend/src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

// Toggle between old and new version
import App from './ImprovedApp';  // New version
// import App from './App';       // Old version

import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
```

### Option 2: Direct Migration

If you want to fully migrate to the new version:

1. **Backup your current code**:
```bash
git commit -m "Backup before migration"
```

2. **Replace old components**:
```bash
# Backup old App.js
mv src/App.js src/App.old.js

# Use new App
mv src/ImprovedApp.jsx src/App.js
```

3. **Update imports** in `src/index.js`:
```javascript
import App from './App';  // Now points to ImprovedApp
```

4. **Update component imports** in App.js:
```javascript
// These imports should already be correct in ImprovedApp
import ImprovedPromptForm from './components/ImprovedPromptForm';
import ImprovedResultBox from './components/ImprovedResultBox';
```

## Component Mapping

| Old Component | New Component | Status |
|--------------|---------------|---------|
| `PromptForm.jsx` | `ImprovedPromptForm.jsx` | Enhanced |
| `ResultBox.jsx` | `ImprovedResultBox.jsx` | Enhanced |
| `ModalitySelector.jsx` | Same | No changes |
| N/A | `Toast.jsx` | New |
| N/A | `History.jsx` | New |

## API Changes

### Backend

The backend has improved error handling and validation but is **backward compatible**. No changes required to API calls.

New endpoints available:
- `GET /health` - Health check
- `GET /models` - Get available models

### Frontend API Client

The API client now includes better error handling:

```javascript
// Old way (still works)
import { generatePrompt } from './api';

// New way (with error handling)
import { generatePrompt, APIError } from './api';

try {
  const result = await generatePrompt(data);
} catch (err) {
  if (err instanceof APIError) {
    console.error('API Error:', err.message, err.status);
  }
}
```

## Configuration Changes

### New Centralized Config

All models and validation rules now live in `config.js`:

```javascript
// Old way - scattered across files
// validation.js had rules
// PromptForm.jsx had model lists

// New way - centralized in config.js
import { MODELS, REQUIRED_FIELDS, TEMPLATES } from './config';
```

### Environment Variables

Create `.env` files from examples:

```bash
# Backend
cp backend/.env.example backend/.env

# Frontend
cp frontend/.env.example frontend/.env
```

## Feature Adoption

### Using Toast Notifications

Replace `alert()` calls:

```javascript
// Old way
alert('Success!');
alert('Error occurred');

// New way
import { useToast } from './hooks/useToast';

function MyComponent() {
  const { success, error } = useToast();

  success('Operation successful!');
  error('Something went wrong');
}
```

### Using History Feature

```javascript
import { usePromptHistory } from './hooks/useLocalStorage';

function MyComponent() {
  const { history, addToHistory, toggleFavorite } = usePromptHistory();

  // Add to history
  addToHistory({
    modality: 'image',
    model: 'dalle-3',
    inputs: {...},
    prompt: '...'
  });

  // Mark as favorite
  toggleFavorite(itemId);
}
```

### Using Templates

Templates are automatically available in the form:

```javascript
// Templates defined in config.js
import { TEMPLATES } from './config';

// Available templates
TEMPLATES.image.portrait  // Portrait photography preset
TEMPLATES.image.landscape // Landscape preset
TEMPLATES.video.cinematic // Cinematic video preset
```

## Testing Your Migration

### 1. Backend Tests

```bash
cd backend
pip install -r requirements.txt
pytest
```

Expected output: All tests passing

### 2. Frontend Tests

```bash
cd frontend
npm install
npm test
```

### 3. Manual Testing Checklist

- [ ] Generate image prompt
- [ ] Generate video prompt
- [ ] Generate voice prompt
- [ ] Copy prompt to clipboard
- [ ] Export as TXT
- [ ] Export as JSON
- [ ] Save to history
- [ ] Mark as favorite
- [ ] Load from history
- [ ] Use template
- [ ] Test validation errors
- [ ] Test on mobile device

## Rollback Procedure

If you need to rollback:

```bash
# Restore from backup
git checkout HEAD~1

# Or manually
mv src/App.old.js src/App.js
```

## Common Issues

### Issue: Import errors

**Solution**: Make sure all new files are in place:
```bash
# Check if files exist
ls src/components/ImprovedPromptForm.jsx
ls src/components/ImprovedResultBox.jsx
ls src/components/Toast.jsx
ls src/hooks/useToast.js
```

### Issue: Styles not loading

**Solution**: Import CSS files:
```javascript
import './styles/ImprovedApp.css';
import './styles/ImprovedForm.css';
import './styles/ImprovedResultBox.css';
import './styles/Toast.css';
import './styles/History.css';
```

### Issue: LocalStorage errors

**Solution**: Clear browser storage:
```javascript
// In browser console
localStorage.clear();
```

### Issue: Backend validation too strict

**Solution**: Check `.env` configuration:
```bash
# In backend/.env
MAX_TEXT_LENGTH=2000
MAX_DURATION_SECONDS=60
```

## Performance Considerations

The improved version:
- Uses React hooks for better performance
- Implements proper memoization
- Reduces unnecessary re-renders
- Uses localStorage for offline capability

No performance degradation expected. In fact, the app should be faster due to optimizations.

## Support

If you encounter issues during migration:

1. Check this guide for solutions
2. Review the README.md for setup instructions
3. Check browser console for errors
4. Verify backend logs in `prompt_generator.log`
5. Open an issue on GitHub with:
   - Error messages
   - Steps to reproduce
   - Browser/environment info

## Next Steps

After successful migration:

1. Review new features in README.md
2. Customize templates in `config.js`
3. Adjust styling in CSS files
4. Set up production deployment
5. Configure monitoring and logging

---

**Questions?** Open an issue or check the documentation.
