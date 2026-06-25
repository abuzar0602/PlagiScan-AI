import { CircularProgressbar } from
"react-circular-progressbar";

import
"react-circular-progressbar/dist/styles.css";

function SimilarityMeter({ value }) {

  return (
    <div
      style={{
        width: 180,
        margin: "20px auto"
      }}
    >
      <CircularProgressbar
        value={value}
        text={`${value}%`}
      />
    </div>
  );
}

export default SimilarityMeter;