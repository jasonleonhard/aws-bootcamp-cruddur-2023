import "./DesktopNavigation.css";
import { ReactComponent as Logo } from "./svg/logo.svg";
import DesktopNavigationLink from "../components/DesktopNavigationLink";
import CrudButton from "../components/CrudButton";
import ProfileInfo from "../components/ProfileInfo";

export default function DesktopNavigation(props) {
  let button;
  let profile;
  let notificationsLink;
  let messagesLink;
  let profileLink;
  if (props.user) {
    button = <CrudButton setPopped={props.setPopped} />;
    profile = <ProfileInfo user={props.user} />;
    // profile = <ProfileInfo user={"worf"} />;
    notificationsLink = (
      <DesktopNavigationLink
        url="/notifications"
        name="Notifications"
        handle="notifications"
        active={props.active}
      />
    );
    messagesLink = (
      <DesktopNavigationLink
        url="/messages"
        name="Messages"
        handle="messages"
        active={props.active}
      />
    );
    profileLink = <DesktopNavigationLink 
      url="/@jasonleonhard" 
      name="Profile"
      handle="profile"
      active={props.active} />
  }
    // profileLink = (
    //   <DesktopNavigationLink
    //     url="/@jasonleonhard"
    //     name="Profile"
    //     handle="profile"
    //     active={props.active}
    //   />
    // );
    // profileLink = (
    //   <DesktopNavigationLink
    //     url="/@worf"
    //     name="Profile"
    //     handle="profile"
    //     active={props.active}
    //   />
    // );
    // profileLink = (
    //   <DesktopNavigationLink
    //     url="/@worf"
    //     name="Profile"
    //     handle="profile"
    //     active={props.active}
    //   />
    // );
    // profileLink = (
    //   <DesktopNavigationLink
    //     url="/@jasonleonhard"
    //     name="Profile"
    //     handle="profile"
    //     active={props.active}
    //   />
    // );

  return (
    <nav>
      <Logo className="logo" />
      <DesktopNavigationLink
        url="/"
        name="Home"
        handle="home"
        active={props.active}
      />
      {notificationsLink}
      {messagesLink}
      {profileLink}
      <DesktopNavigationLink
        url="/health"
        name="Health"
        handle="health"
        active={props.active}
      />
      <DesktopNavigationLink
        url="/routes"
        name="Routes"
        handle="routes"
        active={props.active}
      />
      <DesktopNavigationLink
        url="/#"
        name="More"
        handle="more"
        active={props.active}
      />
      {button}
      {profile}
    </nav>
  );
}
