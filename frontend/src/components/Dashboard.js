import React from 'react';

function Dashboard() {
return (
<div>
    <h2>Analytics Dashboard</h2>
    <iframe src="http://grafana.local/public-dashboards/54a021cb6f4746ee8a2a39de82b1259c" width="450" height="200" frameborder="0"></iframe>
</div>
);
}

export default Dashboard;