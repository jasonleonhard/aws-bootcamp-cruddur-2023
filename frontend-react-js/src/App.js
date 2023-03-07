import "./App.css";

import ConfirmationPage from "./pages/ConfirmationPage";
import HealthPage from "./pages/HealthPage";
import HomeFeedPage from "./pages/HomeFeedPage";
import MessageGroupPage from "./pages/MessageGroupPage";
import MessageGroupsPage from "./pages/MessageGroupsPage";
import NotificationsPage from "./pages/NotificationsPage";
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
  // WIP: only seeing @jasonleonhard at top of page but no content below
  {
    path: "/@:handle",
    element: <UserFeedPage />,
  },
  // does render messages for user sort of 
  // https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/messages
  {
    path: "/messages",
    element: <MessageGroupsPage />,
  },
  // does render messages for user sort of when clicked
  // https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/messages/@jasonleonhard
  {
    path: "/messages/@:handle",
    element: <MessageGroupPage />,
  },
  {
    path: "/signup",
    element: <SignupPage />,
  },
  {
    path: "/signIn",
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
  // renders notifications page @ /notifications front and
  // front: https://3000-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/notifications 
  // backend api: https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/activities/notifications
  {
    path: "/notifications",
    element: <NotificationsPage />,
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
