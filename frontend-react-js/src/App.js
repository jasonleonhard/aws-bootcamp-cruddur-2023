import "./App.css";

import ConfirmationPage from "./pages/ConfirmationPage";
import HealthPage from "./pages/HealthPage";
import HomeFeedPage from "./pages/HomeFeedPage";
import MessageGroupPage from "./pages/MessageGroupPage";
import MessageGroupsPage from "./pages/MessageGroupsPage";
import RecoverPage from "./pages/RecoverPage";
import RoutesPage from "./pages/RoutesPage";
import SignInPage from "./pages/SignInPage";
import SignupPage from "./pages/SignupPage";
import UserFeedPage from "./pages/UserFeedPage";

import React from "react";
// import process from "process";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomeFeedPage />,
  },
  {
    path: "/routes",
    element: <RoutesPage />,
  },
  {
    path: "/health",
    element: <HealthPage />,
  },
  {
    path: "/@:handle",
    element: <UserFeedPage />,
  },
  {
    path: "/messages",
    element: <MessageGroupsPage />,
  },
  {
    path: "/messages/@:handle",
    element: <MessageGroupPage />,
  },
  {
    path: "/signup",
    element: <SignupPage />,
  },
  {
    path: "/signin",
    element: <SignInPage />,
  },
  {
    path: "/confirm",
    element: <ConfirmationPage />,
  },
  {
    path: "/forgot",
    element: <RecoverPage />,
  },
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
