    def getScore_Label(self, bboxes):
        if len(bboxes) == 0:
            return
        else:
            bbox = bboxes[0]
            self.bbx.append([int(bbox[1]), int(bbox[3]), int(bbox[0]) , int(bbox[2])])
            self.scores.append(bbox[4])
    
    def process_traffic_sign(self, frame, bboxes):
        if len(bboxes) != 0:
            self.getScore_Label(bboxes)
            signs = np.zeros_like(frame)
            for i in self.bbx:
                signs = frame[i[0]:i[1], i[2]:i[3]]

            if(signs.shape[0] > 20 and signs.shape[1] > 20):
                return image_to_string(signs)

    def filter_traffic_sign(self, bboxes):
        for i, bbox in enumerate(bboxes):
            if(self.classes[bbox[5]] == "stop sign"):
                return [bbox]
        return []
