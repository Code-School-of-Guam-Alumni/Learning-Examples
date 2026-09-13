import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "./AuthContext";

export function ProtectedRoute() {
  const { loading, user } = useAuth();

  if (loading) return <p>Loading session…</p>;
  if (!user) return <Navigate to="/login" replace />;

  return <Outlet />;
}
