import { Link } from "react-router-dom";

import { ReactComponent as HealthIcon } from "./svg/heart.svg";
import { ReactComponent as HomeIcon } from "./svg/home.svg";
import { ReactComponent as MessagesIcon } from "./svg/messages.svg";
import { ReactComponent as MoreIcon } from "./svg/more.svg";
import { ReactComponent as NotificationsIcon } from "./svg/notifications.svg";
import { ReactComponent as ProfileIcon } from "./svg/profile.svg";
import { ReactComponent as RoutesIcon } from "./svg/routes.svg";

export default function DesktopNavigationLink(props) {
  const classes = () => {
    const classes = ["primary"];
    if (props.handle === props.active) {
      classes.push("active");
    }
    return classes.join(" ");
  };

  const icon = () => {
    switch (props.handle) {
      case "home":
        return <HomeIcon className="icon" />;
      // break;
      case "notifications":
        return <NotificationsIcon className="icon" />;
      // break;
      case "profile":
        return <ProfileIcon className="icon" />;
      // break;
      case "more":
        return <MoreIcon className="icon" />;
      // break;
      case "messages":
        return <MessagesIcon className="icon" />;
      // break;
      case "routes":
        return <RoutesIcon className="icon" />;
      // break;
      case "health":
        return <HealthIcon className="icon" />;
      // break;
    }
  };

  return (
    <Link to={props.url} className={classes()} href="#">
      {icon()}
      <span>{props.name}</span>
    </Link>
  );
}
