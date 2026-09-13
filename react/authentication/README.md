# React Session and Protected-Route Reference

These reconstructed React files show the completed browser-side pattern for the CSG frontend-authentication lessons:

- keep the token in one session boundary;
- restore the session when the application loads;
- attach the token to API requests;
- redirect unauthenticated users away from protected routes;
- never put provider or server secrets in frontend code.

The files are intentionally API-client agnostic. Connect `login`, `loadCurrentUser`, and the task API calls to the application's existing Axios layer.
