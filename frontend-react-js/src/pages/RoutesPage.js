import "./RoutesPage.css";
import React from "react";
import { Link } from "react-router-dom";

import DesktopNavigation from "../components/DesktopNavigation";
import DesktopSidebar from "../components/DesktopSidebar";

// [TODO] Authentication
import Cookies from "js-cookie";

export default function RoutesPage() {
  const [routes, setRoutes] = React.useState([]);
  const [popped, setPopped] = React.useState(false);
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);

  const loadData = async () => {
    try {
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/routes`;
      const res = await fetch(backend_url, {
        method: "GET",
      });
      let resJson = await res.json();
      if (res.status === 200) {
        // console.log(resJson);
        setRoutes(resJson);
      } else {
        console.log(res);
      }
    } catch (err) {
      console.log(err);
    }
  };

  const checkAuth = async () => {
    console.log("checkAuth");
    // [TODO] Authentication
    if (Cookies.get("user.logged_in")) {
      setUser({
        display_name: Cookies.get("user.name"),
        handle: Cookies.get("user.username"),
      });
    }
  };

  React.useEffect(() => {
    // prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadData();
    checkAuth();
  }, []);

  return (
    <article>
      <DesktopNavigation user={user} active={"routes"} setPopped={setPopped} />
      <div className="content">
        <h1>Available Routes:</h1>
        <ul>
          {routes.map((route, index) => (
            <li key={index}>
              <Link className="routes" to={route.url}>
                {route.url}
              </Link>
            </li>
          ))}
        </ul>
      </div>
      <DesktopSidebar user={user} />
    </article>
  );
}
