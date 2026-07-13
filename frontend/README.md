# Frontend - Augment Knowledge Workspace

React (Vite) frontend for the Augment Knowledge Workspace project.

## Local Setup

```bash
npm install
npm run dev
```

App runs at `http://localhost:5173`, proxies `/api` calls to the backend at `http://localhost:8000`.

## Structure

```
src/
  components/  -> reusable UI components
  pages/       -> route-level pages (Login, Dashboard, Documents, Chat)
  services/    -> API client (axios)
  hooks/       -> custom React hooks
  context/     -> auth/global state context
```

## Milestone Mapping

- **Milestone 2**: auth pages, document upload UI, frontend-backend integration
- **Milestone 3**: AI chat interface
- **Milestone 4**: production build via Docker
