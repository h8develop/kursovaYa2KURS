import React from 'react';

function Dashboard() {
return (
<div>
    <h2>Analytics Dashboard</h2>
    <iframe src="http://grafana.local/public-dashboards/88a41d22e115470eb2451314d96643fd" width="450" height="200" frameborder="0"></iframe>
</div>
);
}

export default Dashboard;