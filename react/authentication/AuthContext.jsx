import { createContext, useContext, useEffect, useMemo, useState } from "react";

const AuthContext = createContext(null);

export function AuthProvider({ api, children }) {
  const [token, setToken] = useState(() => window.localStorage.getItem("token"));
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(Boolean(token));

  useEffect(() => {
    if (!token) {
      setUser(null);
      setLoading(false);
      return;
    }

    api.loadCurrentUser(token)
      .then(setUser)
      .catch(() => {
        window.localStorage.removeItem("token");
        setToken(null);
        setUser(null);
      })
      .finally(() => setLoading(false));
  }, [api, token]);

  const value = useMemo(() => ({
    user,
    token,
    loading,
    login(nextToken) {
      window.localStorage.setItem("token", nextToken);
      setLoading(true);
      setToken(nextToken);
    },
    logout() {
      window.localStorage.removeItem("token");
      setToken(null);
      setUser(null);
    },
  }), [loading, token, user]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used inside AuthProvider");
  return context;
}
