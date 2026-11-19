# React Session and Protected-Route Reference

These reconstructed React files show the completed browser-side pattern for the CSG frontend-authentication lessons:

- keep the token in one session boundary;
- restore the session when the application loads;
- attach the token to API requests;
- redirect unauthenticated users away from protected routes;
- never put provider or server secrets in frontend code.

The files are intentionally API-client agnostic. Connect `login`, `loadCurrentUser`, and the task API calls to the application's existing Axios layer.

## Connect this reference to the current guides

This is the token-based checkpoint used by the Cohort 3 / Lance path. Lance keeps using token authentication. Cohort 4 onward uses the matched [Rails session guide](https://github.com/Code-School-of-Guam-Alumni/Resources/blob/main/web-development/03-rails/guide_rails_api_cookie_authentication.md) and [React session guide](https://github.com/Code-School-of-Guam-Alumni/Resources/blob/main/web-development/04-react/guide_react_cookie_authentication.md). The cookie guides use a same-origin `/api` proxy in Vite and Netlify, so Safari does not need third-party cookies. Do not mix token storage from this snapshot into the cookie/CSRF implementation.

On Mac or WSL Ubuntu, start Rails with `rails server` on 3000. Verify the API in HTTPie desktop first, one tab per request and inputs in Params rows. Then start Vite with `npm run dev` on 5173. Use one Axios client with `baseURL: import.meta.env.VITE_API_BASE_URL`; locally set `VITE_API_BASE_URL=http://localhost:3000/api/v1`. Components use relative resource paths. Follow the [required branch workflow](https://github.com/Code-School-of-Guam-Alumni/Resources/blob/main/web-development/02-git-github/branches_and_pull_requests.md) for changes.

The current [Render/Netlify guide](https://github.com/Code-School-of-Guam-Alumni/Resources/blob/main/web-development/05-deployment/guide_deployment_to_render_and_netlify.md) defines deployment; recorded snapshots remain unchanged. WSL-specific steps are **verified by doc review**, not executed on Windows.
