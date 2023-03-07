import "./UserFeedPage.css";
import React from "react";
import { useParams } from "react-router-dom";

import DesktopNavigation from "../components/DesktopNavigation";
import DesktopSidebar from "../components/DesktopSidebar";
import ActivityFeed from "../components/ActivityFeed";
import ActivityForm from "../components/ActivityForm";
// import ReplyForm from "../components/ReplyForm";

// [TODO] Authentication
import Cookies from "js-cookie";

export default function UserFeedPage() {
  const [activities, setActivities] = React.useState([]);
  const [popped, setPopped] = React.useState([]);
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);
  
  // const [replyActivity, setReplyActivity] = React.useState({});
  // const [poppedReply, setPoppedReply] = React.useState(false);


  const params = useParams();
  const title = `@${params.handle}`;

  const loadData = async () => {
    try {
      console.log(`hi ${title}`)
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/activities/${title}`;
      // alert(`user feed page: ${title} aka @jasonleonhard`)
      // alert(`user feed page: ${JSON.stringify(params) + ' aka "handle":"jasonleonhard"}' }`)
      // alert('DesktopNavigation DesktopSidebar ActivityForm ActivityFeed ')
      const res = await fetch(backend_url, {
        method: "GET",
      });
      let resJson = await res.json();
      if (res.status === 200) {
        setActivities(resJson);
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
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadData();
    checkAuth();
  }, []);

  return (
    <article>
      <DesktopNavigation user={user} active={"profile"} setPopped={setPopped} />
      <div className="content">
        <ActivityForm popped={popped} setActivities={setActivities} />
        <ActivityFeed title={title} activities={activities} />
        
        {/* <ActivityForm
          popped={popped}
          setPopped={setPopped}
          setActivities={setActivities}
        />
        <ReplyForm
          activity={replyActivity}
          popped={poppedReply}
          setPopped={setPoppedReply}
          setActivities={setActivities}
          activities={activities}
        />
        <ActivityFeed
          title="Profile"
          setReplyActivity={setReplyActivity}
          setPopped={setPoppedReply}
          activities={activities}
        /> */}

      </div>
      <DesktopSidebar user={user} />
    </article>
  );
}
